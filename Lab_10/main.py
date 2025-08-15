from Conta import Conta
client1 = Conta("Alberto",1)
print(client1.getSaldo())# out: 0 
client1.deposito(2) 
print(client1.getSaldo())# out: 2 
print(client1.deposito(-2))

