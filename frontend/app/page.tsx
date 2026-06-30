import { DashboardShell } from "@/components/layout/dashboard-shell";
import { BrainDumpSection } from "@/components/sections/brain-dump-section";
import { LiveSelectionSection } from "@/components/sections/live-selection-section";
import { TargetLockSection } from "@/components/sections/target-lock-section";

export default function Page() {
  return (
    <DashboardShell>
      <div>
        <h1 className="text-2xl font-bold text-gray-900 mb-1">
          New AI Campaign
        </h1>
        <p className="text-sm text-gray-500">
          Configure target platforms and provide raw input for contextual
          processing.
        </p>
      </div>

      <TargetLockSection />
      <BrainDumpSection />
      <LiveSelectionSection />
    </DashboardShell>
  );
}
