export function LiveDot({ label }: { label: string }) {
  return (
    <div className="flex items-center gap-2 text-xs font-medium text-gray-500">
      <span className="relative flex h-2 w-2 mr-1">
        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75" />
        <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500" />
      </span>
      {label}
    </div>
  );
}
