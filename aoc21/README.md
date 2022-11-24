# Run days

For example, to run day 1:

```typescript
// Run from root
deno run --allow-read day1/day1a.ts
deno run --allow-read day1/day1b.ts
```

# Run tests

For example, to run day 1 tests:

```typescript
// Run from root
deno test --allow-read day1/
```

# Generate daily files

For example, to generate files for day 1:

```typescript
// Run from root
deno run --unstable --allow-read --allow-write template/day.ts 1
```
