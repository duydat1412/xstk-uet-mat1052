"use client";

import React, { useEffect, useRef } from "react";
import katex from "katex";
import { cn } from "@/lib/utils";

interface MathBlockProps {
  math: string;
  display?: boolean;
  className?: string;
}

export function MathBlock({ math, display = false, className }: MathBlockProps) {
  const containerRef = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    if (containerRef.current) {
      try {
        katex.render(math, containerRef.current, {
          displayMode: display,
          throwOnError: false,
        });
      } catch (e) {
        containerRef.current.textContent = math;
      }
    }
  }, [math, display]);

  return (
    <span
      ref={containerRef}
      className={cn(
        display
          ? "block my-2 overflow-x-auto text-center py-2"
          : "inline-block px-0.5",
        className
      )}
    >
      {math}
    </span>
  );
}
