import { useState, useEffect } from "react";

export default function Typewriter({ words, typingSpeed = 100, deletingSpeed = 50, delayBetween = 1500 }: { words: string[], typingSpeed?: number, deletingSpeed?: number, delayBetween?: number }) {
  const [text, setText] = useState("");
  const [isDeleting, setIsDeleting] = useState(false);
  const [wordIndex, setWordIndex] = useState(0);

  useEffect(() => {
    const currentWord = words[wordIndex];
    let timeoutId: NodeJS.Timeout;

    if (isDeleting) {
      timeoutId = setTimeout(() => {
        setText((prev) => prev.slice(0, -1));
        if (text === "") {
          setIsDeleting(false);
          setWordIndex((prev) => (prev + 1) % words.length);
        }
      }, deletingSpeed);
    } else {
      timeoutId = setTimeout(() => {
        setText(currentWord.slice(0, text.length + 1));
        if (text === currentWord) {
          timeoutId = setTimeout(() => setIsDeleting(true), delayBetween);
        }
      }, typingSpeed);
    }

    return () => clearTimeout(timeoutId);
  }, [text, isDeleting, wordIndex, words, typingSpeed, deletingSpeed, delayBetween]);

  return (
    <span>
      {text}
      <span className="cursor">|</span>
      <style>{`
        .cursor {
          animation: blink 1s step-end infinite;
          color: var(--accent);
          font-weight: 300;
        }
        @keyframes blink {
          50% { opacity: 0; }
        }
      `}</style>
    </span>
  );
}
