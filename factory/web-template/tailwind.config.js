/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                hyper: {
                    bg: '#0a0a0a',
                    glass: 'rgba(255, 255, 255, 0.03)',
                    border: 'rgba(255, 255, 255, 0.1)',
                    accent: '#00ccff',
                    success: '#00ffaa',
                    warning: '#ffaa00',
                    danger: '#ff4444',
                }
            },
            backdropBlur: {
                xs: '2px',
            }
        },
    },
    plugins: [],
}
