function shareTwitter() {
    if (!window.userResult) return;
    const { name, freq, creates } = window.userResult;
    const text = `My frequency: ${freq} Hz creates ${creates.universe.toLocaleString()} Hz reality with the Universe 🌌 Every frequency creates. What does yours create?`;
    const url = window.location.href;
    window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`, '_blank');
}

function copyLink() {
    if (!window.userResult) return;
    const { freq, creates } = window.userResult;
    const text = `My frequency: ${freq} Hz creates ${creates.universe.toLocaleString()} Hz reality. Every frequency creates value. Discover yours at ${window.location.href}`;

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