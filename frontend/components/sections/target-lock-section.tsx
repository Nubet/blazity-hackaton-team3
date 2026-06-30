import { PlatformCard } from "@/components/ui/platform-card";
import { StepHeader } from "@/components/ui/step-header";

export function TargetLockSection() {
  return (
    <div>
      <StepHeader marker="1" title="Target Lock" />

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <PlatformCard
          platform="linkedin"
          title="LinkedIn"
          subtitle="B2B, Professional, Networking"
          selected
        />
        <PlatformCard
          platform="instagram"
          title="Instagram"
          subtitle="Visual, Lifestyle, Engagement"
          selected
        />
        <PlatformCard
          platform="x"
          title="X (Twitter)"
          subtitle="Short-form, News, Trends"
        />
      </div>
    </div>
  );
}
