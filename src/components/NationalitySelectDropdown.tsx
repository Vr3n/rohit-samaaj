"use client";

import { useState } from "react";
import { Check, ChevronsUpDown } from "lucide-react";
import { cn } from "~/lib/utils";
import { Button } from "./ui/button";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
} from "~/components/ui/command";
import { Popover, PopoverContent, PopoverTrigger } from "./ui/popover";
import { nationalityList } from "~/constants/nationalityList";
import "../../string.extensions";
import type { UseFormSetValue } from "react-hook-form";
import { ScrollArea } from "./ui/scroll-area";

const NationalitySelectDropdown = (props: {
  setValue: UseFormSetValue<any>;
  className?: string;
}) => {
  const [open, setOpen] = useState<boolean>(false);
  const [select, setSelect] = useState<string>("indian");

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          role="combobox"
          aria-expanded={open}
          title="nationality select"
          className={cn("justify-between", props.className)}
        >
          {select
            ? nationalityList.find((nationality) => nationality === select)
            : "Select Nationality"}
          <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent>
        <ScrollArea>
          <Command>
            <CommandInput placeholder="Select nationality..." />
            <CommandEmpty>Nationality not found.</CommandEmpty>
            <CommandGroup>
              {nationalityList.map((nationality: string) => (
                <CommandItem
                  key={nationality}
                  value={nationality}
                  onSelect={(value) => {
                    setSelect(value);
                    props.setValue("nationality", value);
                    setOpen(false);
                  }}
                >
                  <Check
                    className={cn(
                      "mr-2 h-4 w-4",
                      select === nationality ? "opacity-100" : "opacity-0"
                    )}
                  />
                  {nationality.titleCase()}
                </CommandItem>
              ))}
            </CommandGroup>
          </Command>
        </ScrollArea>
      </PopoverContent>
    </Popover>
  );
};

export default NationalitySelectDropdown;
