import type { ReactNode } from "react";
import { PlatformIconBadge } from "@/components/ui/platform-icon-badge";
import {
  AssetCurationTable,
  type AssetRow,
} from "./asset-curation-table";

type Platform = "linkedin" | "instagram" | "x";

type Props = {
  platform: Platform;
  title: string;
  target: string;
  copyLabel: string;
  copy: ReactNode;
  hashtagsClassName: string;
  hashtags: string;
  rows: AssetRow[];
};

export function PlatformReport({
  platform,
  title,
  target,
  copyLabel,
  copy,
  hashtagsClassName,
  hashtags,
  rows,
}: Props) {
  return (
    <div className="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden flex flex-col">
      <div className="p-5 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <div className="flex items-center gap-3">
          <PlatformIconBadge platform={platform} size="sm" weight="bold" />
          <div>
            <h3 className="text-sm font-semibold text-gray-900">{title}</h3>
            <p className="text-xs text-gray-500">Target: {target}</p>
          </div>
        </div>
      </div>

      <div className="p-5 border-b border-gray-100">
        <div className="text-xs font-medium text-gray-400 uppercase tracking-wider mb-2">
          {copyLabel}
        </div>
        <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 text-sm text-gray-700 leading-relaxed">
          {copy}
          <br />
          <br />
          <span className={hashtagsClassName}>{hashtags}</span>
        </div>
      </div>

      <AssetCurationTable rows={rows} />
    </div>
  );
}
