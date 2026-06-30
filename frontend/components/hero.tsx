"use client";

import { useEffect } from "react";
import Link from "next/link";
import { ArrowRight, Plus, Shapes } from "@phosphor-icons/react/dist/ssr";
import { renderCanvas } from "@/components/ui/canvas";
import { Button } from "@/components/ui/button";

export function Hero() {
  useEffect(() => {
    renderCanvas();
  }, []);

  return (
    <section id="home" className="relative h-screen flex items-center justify-center overflow-hidden bg-white">
      <div className="relative z-10 flex flex-col items-center justify-center px-4 text-center animate-fade-in">
        <div className="mb-6 sm:justify-center md:mb-4">
          <div className="relative flex items-center whitespace-nowrap rounded-full border border-gray-200 bg-white/80 backdrop-blur-sm px-3 py-1 text-xs leading-6 text-gray-500">
            <Shapes size={20} className="text-blue-600 mr-1" />
            AI-Powered Content Repurposing
            <Link
              href="/dashboard"
              className="ml-1 flex items-center font-semibold text-blue-600 hover:text-blue-700"
            >
              <div className="absolute inset-0 flex" aria-hidden="true" />
              Try it free
              <ArrowRight size={16} className="ml-0.5" />
            </Link>
          </div>
        </div>

        <div className="mb-10 mt-4 md:mt-6">
          <div className="px-2">
            <div className="relative mx-auto h-full max-w-7xl border border-blue-500/30 p-6 [mask-image:radial-gradient(800rem_96rem_at_center,white,transparent)] md:px-12 md:py-20">
              <Plus
                size={40}
                weight="bold"
                className="text-blue-500 absolute -left-5 -top-5"
              />
              <Plus
                size={40}
                weight="bold"
                className="text-blue-500 absolute -bottom-5 -left-5"
              />
              <Plus
                size={40}
                weight="bold"
                className="text-blue-500 absolute -right-5 -top-5"
              />
              <Plus
                size={40}
                weight="bold"
                className="text-blue-500 absolute -bottom-5 -right-5"
              />
              <h1 className="flex select-none flex-col px-3 py-2 text-center text-5xl font-semibold leading-none tracking-tight text-gray-900 md:text-8xl">
                The Smartest Way to Repurpose Content.
              </h1>
            </div>
          </div>

          <p className="mx-auto mb-10 mt-8 max-w-2xl px-6 text-sm text-gray-500 sm:px-6 md:max-w-4xl md:px-20 lg:text-lg">
            Paste your raw ideas. Pick a platform. Get a finished post — tailored
            for LinkedIn, Instagram, or X with the right tone and format.
          </p>

          <div className="flex justify-center gap-3">
            <Link href="/dashboard">
              <Button size="lg">Start Creating</Button>
            </Link>
          </div>
        </div>
      </div>

      <canvas
        className="pointer-events-none absolute inset-0 mx-auto"
        id="canvas"
      />
    </section>
  );
}
