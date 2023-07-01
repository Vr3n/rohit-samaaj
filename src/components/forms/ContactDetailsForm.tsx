"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import type z from "zod";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "../ui/form";
import { Input } from "../ui/input";
import { useRef, useState } from "react";
import { Card, CardContent, CardFooter, CardHeader } from "../ui/card";
import { Separator } from "../ui/separator";
import { Button } from "../ui/button";
import { cn } from "~/lib/utils";
import { Loader } from "lucide-react";
import { useToast } from "../ui/use-toast";
import { contactDetailsFormSchema } from "~/schemas/surveyFormSchema";
import { Checkbox } from "../ui/checkbox";

const ContactDetailsForm = () => {
  const { toast } = useToast();
  const watchMobileNumberRef = useRef<string>("");

  const [isFormSubmitting, setIsFormSubmitting] = useState<boolean>(false);

  const form = useForm<z.infer<typeof contactDetailsFormSchema>>({
    resolver: zodResolver(contactDetailsFormSchema),
    mode: "onChange",
    defaultValues: {
      mobile: {
        mobile_number: undefined,
        is_whatsapp: undefined,
      },
      email: undefined,
    },
  });

  const { isDirty, isValid } = form.formState;

  function onSubmit(values: z.infer<typeof contactDetailsFormSchema>) {
    setIsFormSubmitting(true);
    setTimeout(() => {
      toast({
        title: "You submitted the following values:",
        description: (
          <pre className="w[340px] mt-2 rounded-md bg-slate-950 p-4">
            <code className="text-white">
              {JSON.stringify(values, null, 2)}
            </code>
          </pre>
        ),
      });
      setIsFormSubmitting(false);
    }, 3000);
  }

  watchMobileNumberRef.current = form.watch("mobile.mobile_number");

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <Card>
          <CardHeader>
            <h4 className="-mb-2 text-xl">Contact Details</h4>
            <p className="text-sm text-gray-400">
              Your Mobile number and email address.
            </p>
          </CardHeader>
          <CardContent>
            <Separator />
            <div className="grid gap-x-6">
              <FormField
                control={form.control}
                name="mobile.mobile_number"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex flex-col gap-2">
                    <FormItem>
                      <FormLabel>Mobile Number</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="Enter your mobile number."
                          className={cn(
                            fieldState.isDirty &&
                              !fieldState.invalid &&
                              "border-green-400",
                            fieldState.error && "border-red-400"
                          )}
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                      {watchMobileNumberRef.current && (
                        <FormDescription
                          className={cn(
                            watchMobileNumberRef.current?.length === 10 &&
                              "text-green-400",
                            watchMobileNumberRef.current?.length > 10 &&
                              "text-red-400",
                            "flex gap-3"
                          )}
                        >
                          {10 - watchMobileNumberRef.current?.length} digits
                          remaining.{" "}
                        </FormDescription>
                      )}
                    </FormItem>
                  </div>
                )}
              />
              <FormField
                control={form.control}
                name="mobile.is_whatsapp"
                render={({ field }) => (
                  <FormItem className="flex flex-row items-center gap-2">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <FormLabel className="text-sm">Is Whatsapp?</FormLabel>
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="email"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex flex-col gap-2">
                    <FormItem>
                      <FormLabel>Email Address</FormLabel>
                      <FormControl>
                        <Input
                          type="email"
                          placeholder="abc@email.com"
                          className={cn(
                            fieldState.isDirty &&
                              !fieldState.invalid &&
                              "border-green-400",
                            fieldState.error && "border-red-400"
                          )}
                          {...field}
                        />
                      </FormControl>
                    </FormItem>
                  </div>
                )}
              />
            </div>
          </CardContent>
          <CardFooter>
            <Button
              disabled={!isDirty || !isValid || !!isFormSubmitting}
              type="submit"
            >
              {" "}
              Submit
              {!!isFormSubmitting && (
                <Loader className="ml-5 animate-spin" />
              )}{" "}
            </Button>
          </CardFooter>
        </Card>
      </form>
    </Form>
  );
};

export default ContactDetailsForm;
