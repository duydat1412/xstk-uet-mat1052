import React from "react";
import katex from "katex";

/**
 * Parses mixed HTML/text and replaces LaTeX formulas delimited by:
 * - $$ ... $$ (display block)
 * - \[ ... \] (display block)
 * - $ ... $ (inline)
 * - \( ... \) (inline)
 * with KaTeX-rendered HTML strings.
 */
export function renderMathInText(text: string): string {
  if (!text) return "";
  // Ensure Unicode NFC normalization so Vietnamese accented characters
  // are precomposed into single code points (prevents NFD mark splitting)
  text = text.normalize("NFC");

  // 1. Block math: $$ ... $$
  let result = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), {
        displayMode: true,
        throwOnError: false,
        strict: "ignore",
      });
    } catch (e) {
      return `$$${math}$$`;
    }
  });

  // 2. Block math: \[ ... \]
  result = result.replace(/\\\[([\s\S]+?)\\\]/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), {
        displayMode: true,
        throwOnError: false,
        strict: "ignore",
      });
    } catch (e) {
      return `\\[${math}\\]`;
    }
  });

  // 3. Inline math: \( ... \)
  result = result.replace(/\\\(([\s\S]+?)\\\)/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), {
        displayMode: false,
        throwOnError: false,
        strict: "ignore",
      });
    } catch (e) {
      return `\\(${math}\\)`;
    }
  });

  // 4. Inline math: $ ... $
  // Matches non-empty text between single dollar signs that does not span newlines
  result = result.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), {
        displayMode: false,
        throwOnError: false,
        strict: "ignore",
      });
    } catch (e) {
      return `$${math}$`;
    }
  });

  return result;
}

export function MathText({
  content,
  className,
  as: Component = "span",
}: {
  content: string;
  className?: string;
  as?: React.ElementType;
}) {
  const html = renderMathInText(content);
  return (
    <Component
      className={className}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
