import Image from "next/image";
import { SmileyWink } from "@phosphor-icons/react/dist/ssr";
import { StatusBadge } from "@/components/ui/status-badge";

type ImageThumb = { kind: "image"; src: string; alt: string };
type MemeThumb = { kind: "meme" };

export type AssetRow = {
  thumb: ImageThumb | MemeThumb;
  name: string;
  reasoning: string;
  status: { variant: "selected" | "rejected" | "moved"; label: string };
  muted?: boolean;
};

function RowThumb({ thumb }: { thumb: ImageThumb | MemeThumb }) {
  if (thumb.kind === "meme") {
    return (
      <div className="w-8 h-8 rounded border border-gray-200 bg-yellow-100 flex items-center justify-center">
        <SmileyWink size={16} weight="fill" className="text-yellow-500" />
      </div>
    );
  }
  return (
    <Image
      src={thumb.src}
      alt={thumb.alt}
      width={32}
      height={32}
      className="w-8 h-8 rounded object-cover border border-gray-200"
    />
  );
}

export function AssetCurationTable({ rows }: { rows: AssetRow[] }) {
  return (
    <div className="p-0 flex-1">
      <div className="px-5 py-3 text-xs font-medium text-gray-400 uppercase tracking-wider border-b border-gray-100">
        Asset Curation
      </div>
      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="border-b border-gray-100 text-xs text-gray-500">
            <th className="font-normal px-5 py-3 w-1/2">Asset</th>
            <th className="font-normal px-5 py-3">AI Reasoning</th>
            <th className="font-normal px-5 py-3 text-right">Action</th>
          </tr>
        </thead>
        <tbody className="text-sm">
          {rows.map((row, idx) => {
            const reasoningTone = row.muted ? "text-gray-400" : "text-gray-500";
            const nameClasses = row.muted
              ? "font-medium text-gray-500 line-through"
              : "font-medium text-gray-900";
            const cellClasses = `px-5 py-3 flex items-center gap-3${
              row.muted ? " opacity-60" : ""
            }`;

            return (
              <tr
                key={idx}
                className="border-b border-gray-50 hover:bg-gray-50/50 transition-colors"
              >
                <td className={cellClasses}>
                  <RowThumb thumb={row.thumb} />
                  <span className={nameClasses}>{row.name}</span>
                </td>
                <td className={`px-5 py-3 text-xs ${reasoningTone}`}>
                  {row.reasoning}
                </td>
                <td className="px-5 py-3 text-right">
                  <StatusBadge variant={row.status.variant}>
                    {row.status.label}
                  </StatusBadge>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
