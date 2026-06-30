type Variant = "selected" | "rejected" | "moved";

const styles: Record<Variant, string> = {
  selected: "bg-green-100 text-green-700",
  rejected: "bg-red-50 text-red-600",
  moved: "bg-yellow-100 text-yellow-700",
};

export function StatusBadge({
  variant,
  children,
}: {
  variant: Variant;
  children: React.ReactNode;
}) {
  return (
    <span
      className={`inline-flex items-center px-2 py-1 rounded text-xs font-medium ${styles[variant]}`}
    >
      {children}
    </span>
  );
}
