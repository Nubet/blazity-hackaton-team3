import { MagicWand } from "@phosphor-icons/react/dist/ssr";
import { LiveDot } from "@/components/ui/live-dot";
import { StepHeader } from "@/components/ui/step-header";
import { PlatformReport } from "./platform-report";
import type { AssetRow } from "./asset-curation-table";

const linkedInRows: AssetRow[] = [
  {
    thumb: {
      kind: "image",
      src: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=100&q=80",
      alt: "Code snippet",
    },
    name: "Code Snippet",
    reasoning: "High professional value. Shows expertise.",
    status: { variant: "selected", label: "Selected (1st)" },
  },
  {
    thumb: {
      kind: "image",
      src: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&q=80",
      alt: "Developer selfie",
    },
    name: "Developer Selfie",
    reasoning: "Adds authenticity to the narrative.",
    status: { variant: "selected", label: "Selected (2nd)" },
  },
  {
    thumb: {
      kind: "image",
      src: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=100&q=80",
      alt: "Pizza photo",
    },
    name: "Pizza Photo",
    reasoning: "Too informal for B2B network.",
    status: { variant: "rejected", label: "Rejected" },
    muted: true,
  },
  {
    thumb: { kind: "meme" },
    name: "Meme",
    reasoning: "Decreases professional authority.",
    status: { variant: "rejected", label: "Rejected" },
    muted: true,
  },
];

const instagramRows: AssetRow[] = [
  {
    thumb: {
      kind: "image",
      src: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&q=80",
      alt: "Developer selfie",
    },
    name: "Developer Selfie",
    reasoning: "Humanizes content. High engagement.",
    status: { variant: "selected", label: "Selected (1st)" },
  },
  {
    thumb: { kind: "meme" },
    name: "Meme",
    reasoning: "Relatable culture reference. Shareable.",
    status: { variant: "selected", label: "Selected (2nd)" },
  },
  {
    thumb: {
      kind: "image",
      src: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=100&q=80",
      alt: "Pizza photo",
    },
    name: "Pizza Photo",
    reasoning: 'Fits "Late night hustle" lifestyle vibe.',
    status: { variant: "selected", label: "Selected (3rd)" },
  },
  {
    thumb: {
      kind: "image",
      src: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=100&q=80",
      alt: "Code snippet",
    },
    name: "Code Snippet",
    reasoning: "Low visual appeal. Hidden at the end.",
    status: { variant: "moved", label: "Moved Last" },
  },
];

export function LiveSelectionSection() {
  return (
    <div>
      <StepHeader
        markerVariant="brand"
        marker={<MagicWand size={12} weight="bold" />}
        title="Live Contextual Selection"
        right={<LiveDot label="Processing Complete" />}
      />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <PlatformReport
          platform="linkedin"
          title="LinkedIn Pipeline"
          target="Tech Professionals"
          copyLabel="Generated Copy (Tech Debt Focus)"
          copy={
            <>
              Pokonywanie długu technologicznego to chleb powszedni każdego
              inżyniera. Po całonocnej walce z architekturą przypominam sobie,
              dlaczego kocham ten zawód. Poniżej fragment rozwiązania, które
              wczoraj uratowało nasz sprint. 🚀💻
            </>
          }
          hashtagsClassName="text-blue-600"
          hashtags="#SoftwareEngineering #TechDebt #Coding"
          rows={linkedInRows}
        />

        <PlatformReport
          platform="instagram"
          title="Instagram Pipeline"
          target="Lifestyle & Vibe"
          copyLabel="Generated Copy (Hustle Focus)"
          copy={
            <>
              Late night hustle! 🌙 Czasem kod nie współpracuje, ale kiedy o 4
              rano wjeżdża pizza, od razu wiadomo, że to będzie dobra noc. Kto z
              Was też najlepiej skupia się, gdy reszta świata śpi? 🍕💻✨
            </>
          }
          hashtagsClassName="text-pink-600"
          hashtags="#nightowl #codinglife #hustle #devvibe"
          rows={instagramRows}
        />
      </div>
    </div>
  );
}
