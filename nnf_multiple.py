import math
x=[3,2,1]
w=[0.5,0.2,0.1]
y=1
b=0.1
n=0.01
for epoch in range(1000):
    z=0
    for i in range(len(x)):
        z+=w[i]*x[i]
    z+=b
    a=1/(1+math.exp(-z))
    error=a-y
    loss=(error)*(error)
    if(loss<0.000001):
        break
    for i in range(len(w)):
        dl_dw=2*error*x[i]
        w[i]=w[i]-n*dl_dw

    if(epoch%100==0):
        print(f"Epoch={epoch},Loss={loss:.6f}")
print("\nFinal weight",w)
print("prediction",a)
print("Loss",loss)

    




        
    

