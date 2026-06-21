import math
x=2
y=1
w=0.5
b=0.1
n=0.01
for epoch in range(1000):
     z=w*x+b
     a=1/(1+math.exp(-z))
     error=a-y
     loss=(error)*(error)
     if loss<0.000001:
          break
     dl_dw=2*error*x
     nw=w-n*dl_dw
     if epoch%100==0:
          print(f"Epoch{epoch},Loss={loss:.6f}")


print("\nFinal weight",w)
print("prediction",a)
print("Loss",loss)



