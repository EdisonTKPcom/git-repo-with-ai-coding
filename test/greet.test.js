import { test } from 'node:test';
import assert from 'node:assert/strict';
import { greet } from '../src/index.js';

// Happy path
await test('greet returns greeting', () => {
    assert.strictEqual(greet('Alice'), 'Hello, Alice!');
});

// Edge: invalid input
await test('greet rejects empty string', () => {
    assert.throws(() => greet(''), /non-empty/);
});
