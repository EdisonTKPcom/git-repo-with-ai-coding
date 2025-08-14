// SPDX-License-Identifier: MIT
// AI-assisted: human-reviewed
export function greet(name) {
    if (typeof name !== 'string' || name.trim() === '') {
        throw new Error('Name must be a non-empty string');
    }
    return `Hello, ${name}!`;
}

if (process.argv[1] === new URL(import.meta.url).pathname) {
    // simple CLI usage
    const arg = process.argv[2] || 'World';

    console.log(greet(arg));
}
