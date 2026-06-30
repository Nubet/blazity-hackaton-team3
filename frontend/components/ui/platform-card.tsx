import { CheckCircle } from "@phosphor-icons/react/dist/ssr";
import { PlatformIconBadge } from "./platform-icon-badge";

type Platform = "linkedin" | "instagram" | "x";

type Props = {
  platform: Platform;
  title: string;
  subtitle: string;
  selected?: boolean;
};

const selectedBorder: Record<Platform, string> = {
  linkedin: "border-2 border-blue-600",
  instagram: "border-2 border-pink-500",
  x: "border-2 border-gray-900",
};

const checkColor: Record<Platform, string> = {
  linkedin: "text-blue-600",
  instagram: "text-pink-500",
  x: "text-gray-900",
};

export function PlatformCard({ platform, title, subtitle, selected }: Props) {
  const base =
    "bg-white rounded-xl p-5 shadow-sm relative cursor-pointer transition-opacity";
  const stateClasses = selected
    ? selectedBorder[platform]
    : "border border-gray-200 opacity-60 hover:opacity-100";

  return (
    <div className={`${base} ${stateClasses}`}>
      {selected ? (
        <div className={`absolute top-4 right-4 ${checkColor[platform]}`}>
          <CheckCircle size={20} weight="fill" />
        </div>
      ) : null}
      <div className="mb-4">
        <PlatformIconBadge platform={platform} size="md" />
      </div>
      <div className="text-sm font-semibold text-gray-900">{title}</div>
      <div className="text-xs text-gray-500 mt-1">{subtitle}</div>
    </div>
  );
}
