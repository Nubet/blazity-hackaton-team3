import Link from "next/link";
import { ArrowRight } from "@phosphor-icons/react/dist/ssr";
import { Button } from "@/components/ui/button";

export function CtaSection() {
  return (
    <section className="bg-blue-600 py-24 px-4">
      <div className="max-w-3xl mx-auto text-center">
        <h2 className="text-4xl font-semibold tracking-tight text-white mb-4">
          Stop reformatting. Start publishing.
        </h2>
        <p className="text-blue-100 mb-10 text-lg">
          Your ideas are already good. FlowForge just makes them fit wherever
          they need to go.
        </p>
        <Link href="/dashboard">
          <Button
            size="lg"
            className="bg-white text-blue-600 hover:bg-blue-50 font-semibold"
          >
            Start Creating
            <ArrowRight size={18} className="ml-2" />
          </Button>
        </Link>
      </div>
    </section>
  );
}
