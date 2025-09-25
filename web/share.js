function shareTwitter() {
    if (!window.userResult) return;
    const { name, freq, resonates } = window.userResult;
    const text = resonates ?
        `My cosmic frequency is ${freq} Hz and I resonate perfectly with the Universe! 🌌✨ What's yours?` :
        `My cosmic frequency is ${freq} Hz, creating unique harmonics with the Universe! 🌟 What's yours?`;
    const url = window.location.href;
    window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`, '_blank');
}

function copyLink() {
    if (!window.userResult) return;
    const { freq, resonates } = window.userResult;
    const text = `My cosmic frequency: ${freq} Hz${resonates ? ' (Perfect resonance!)' : ''} - Discover yours at ${window.location.href}`;

    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            alert('Copied to clipboard!');
        });
    } else {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        alert('Copied to clipboard!');
    }
}