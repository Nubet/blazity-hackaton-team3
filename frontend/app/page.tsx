import { DashboardShell } from "@/components/layout/dashboard-shell";
import { CampaignStudio } from "@/components/studio/campaign-studio";

export default function Page() {
  return (
    <DashboardShell>
      <CampaignStudio />
    </DashboardShell>
  );
}
