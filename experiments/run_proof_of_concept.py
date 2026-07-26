"""Run a lightweight synthetic precision-regime comparison."""
import json, sys
from pathlib import Path
import torch
from torch import nn
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from lapa.controller import LAPAController
from lapa.metrics import effective_bits, precision_histogram
from lapa.training import accuracy, train_epoch

def make_dataset(seed=7):
    g = torch.Generator().manual_seed(seed)
    x = torch.randn(1200, 8, generator=g)
    w = torch.tensor([[1.4,-0.8,0.5,0.2,-1.0,0.7,0.1,-0.4],[-0.6,1.2,-0.7,0.9,0.2,-0.3,1.0,0.4],[0.2,-0.4,1.1,-0.8,0.7,0.5,-0.6,1.2]])
    y = (x @ w.T + 0.15 * torch.randn(1200, 3, generator=g)).argmax(dim=1)
    return x[:900], y[:900], x[900:], y[900:]

def build_model(seed=7):
    torch.manual_seed(seed)
    return nn.Sequential(nn.Linear(8,24), nn.ReLU(), nn.Linear(24,3))

def run(name, epochs=40):
    xtr,ytr,xv,yv = make_dataset(); model=build_model()
    opt=torch.optim.Adam(model.parameters(),lr=0.03); loss_fn=nn.CrossEntropyLoss()
    controller=LAPAController((0.003,0.015),(4,8,16)) if name=='adaptive' else None
    static={'static_8':8,'static_4':4}.get(name)
    assigned=[]; final_loss=0.0
    for _ in range(epochs):
        final_loss,_,bits=train_epoch(model,opt,loss_fn,xtr,ytr,controller,static); assigned.append(bits)
    return {'regime':name,'epochs':epochs,'final_loss':round(final_loss,6),'validation_accuracy':round(accuracy(model,xv,yv),6),'effective_bits':round(effective_bits(assigned),4),'precision_histogram':precision_histogram(assigned)}

def main():
    torch.use_deterministic_algorithms(True)
    results=[run(n) for n in ('fp32','static_8','adaptive','static_4')]
    out=ROOT/'results'/'generated'; out.mkdir(parents=True,exist_ok=True)
    path=out/'synthetic_proof_of_concept.json'; path.write_text(json.dumps(results,indent=2))
    print(json.dumps(results,indent=2)); print(f'\nSaved: {path}')

if __name__=='__main__': main()
