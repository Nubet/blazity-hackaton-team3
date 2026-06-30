import { Hero } from "@/components/hero";
import { HowItWorks } from "@/components/landing/how-it-works";
import { Features } from "@/components/landing/features";
import { Platforms } from "@/components/landing/platforms";
import { CtaSection } from "@/components/landing/cta";

export default function LandingPage() {
  return (
    <main>
      <Hero />
      <HowItWorks />
      <Features />
      <Platforms />
      <CtaSection />
    </main>
  );
}
