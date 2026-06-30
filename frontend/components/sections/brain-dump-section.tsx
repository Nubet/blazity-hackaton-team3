import { Plus } from "@phosphor-icons/react/dist/ssr";
import { AssetThumb } from "@/components/ui/asset-thumb";
import { StepHeader } from "@/components/ui/step-header";

export function BrainDumpSection() {
  return (
    <div>
      <StepHeader marker="2" title="The Brain Dump" />

      <div className="bg-white border border-gray-200 rounded-xl shadow-sm p-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="flex flex-col">
          <label
            htmlFor="brain-dump-text"
            className="text-sm font-medium text-gray-700 mb-2"
          >
            Raw Thoughts
          </label>
          <textarea
            id="brain-dump-text"
            defaultValue="robiłem apkę całą noc, błędy w kodzie, zjadłem pizzę, fajne uczucie"
            className="w-full flex-1 min-h-[160px] bg-gray-50 border border-gray-200 rounded-lg p-4 text-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 resize-none"
          />
        </div>

        <div className="flex flex-col">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-medium text-gray-700">
              Raw Media Assets (4)
            </span>
            <button
              type="button"
              className="text-xs font-medium text-blue-600 hover:text-blue-700 flex items-center gap-1"
            >
              <Plus size={12} /> Upload
            </button>
          </div>
          <div className="flex-1 border-2 border-dashed border-gray-200 rounded-lg bg-gray-50 p-4 grid grid-cols-2 gap-3">
            <AssetThumb
              kind="image"
              src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&q=80"
              alt="Code snippet"
            />
            <AssetThumb
              kind="image"
              src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80"
              alt="Developer selfie"
              objectPosition="top"
            />
            <AssetThumb
              kind="image"
              src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&q=80"
              alt="Pizza photo"
            />
            <AssetThumb kind="meme" label="meme.jpg" />
          </div>
        </div>
      </div>
    </div>
  );
}
