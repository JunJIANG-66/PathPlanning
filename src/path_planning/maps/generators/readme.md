Code to use EmptyMapGenerator:
```
generator = EmptyMapGenerator(
    width=100,
    height=100,
    resolution=0.1,
)

map = generator.generate()

print(map.width)
print(map.height)
```
