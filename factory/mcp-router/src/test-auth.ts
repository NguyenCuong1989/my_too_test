import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';

const JWT_SECRET = 'super-secret-mcp-key';
const token = jwt.sign({ name: 'SystemAdmin', role: 'admin' }, JWT_SECRET);

console.log('Generated Token:', token);

async function testExecute() {
    try {
        const response = await fetch('http://localhost:3000/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({
                tool: 'calculate-harmony',
                arguments: { component: 'G2-Layer' }
            })
        });

        const data = await response.json();
        console.log('Response:', data);
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

testExecute();
