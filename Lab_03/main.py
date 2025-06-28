from CLockDisplay import ClockDisplay

relogio = ClockDisplay()
print("Hora inicial:", relogio.getDisplay())

# Simular 125 minutos (2h05m)
for _ in range(3600):
    relogio.timeTick()
print("Após 125 ticks:", relogio.getDisplay())
