import torch
import torch.optim as optim
import matplotlib.pyplot as plt

t_c = [0.5,14.0,15.0,28.0,11.0,8.0,3.0,-4.0,6.0,13.0,21.0]
t_u = [35.7,55.9,58.2,81.9,56.3,48.9,33.9,21.8,48.4,60.4,68.4]

t_c = torch.tensor(t_c)
t_u = torch.tensor(t_u)

def model(input,w1,w2,b):
    return w1*input + w2*input**2 + b

def loss_fn(t_p,t_c):
    diffs = (t_p - t_c)**2
    return diffs.mean()

def training_loop(n_epochs,optimizer,params,t_u,t_c):
    for epoch in range(1,n_epochs+1):

        t_p = model(t_u,*params)
        loss = loss_fn(t_p,t_c)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch<=5 or epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss {loss.item():.4f}")
    return params

params = torch.tensor([1.0,1.0,0],requires_grad=True)
optimizer = optim.Adam([params],lr=1e-1)
params = training_loop(n_epochs=5000,optimizer=optimizer,params=params,t_u=t_u*0.1,t_c=t_c)

t_p = model(t_u*0.1,*params)
print(t_p)
