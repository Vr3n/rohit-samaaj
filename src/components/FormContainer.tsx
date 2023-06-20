import { cn } from "~/lib/utils";

const FormContainer = ({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) => {
  return <div className={cn("max-w-2xl", className)}>{children}</div>;
};

export default FormContainer;
