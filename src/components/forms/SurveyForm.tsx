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
import NationalitySelectDropdown from "../NationalitySelectDropdown";
import { Button } from "../ui/button";
import { cn } from "~/lib/utils";
import { Loader } from "lucide-react";
import { useToast } from "../ui/use-toast";
import { surveyFormSchema } from "~/schemas/surveyFormSchema";

const SurveyForm = () => {
  const watchAadharNumberRef = useRef<string>("");
  const { toast } = useToast();

  const [isFormSubmitting, setIsFormSubmitting] = useState<boolean>(false);

  const form = useForm<z.infer<typeof surveyFormSchema>>({
    resolver: zodResolver(surveyFormSchema),
    mode: "onChange",
    defaultValues: {
      nationality: "indian",
      aadharNumber: undefined,
      firstName: undefined,
      lastName: undefined,
      motherName: undefined,
      fatherName: undefined,
    },
  });

  const { isDirty, isValid } = form.formState;

  function onSubmit(values: z.infer<typeof surveyFormSchema>) {
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

  watchAadharNumberRef.current = form.watch("aadharNumber");

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <Card>
          <CardHeader>
            <h4 className="-mb-2 text-xl">Personal Details</h4>
            <p className="text-sm text-gray-400">
              your name and unique identity number.
            </p>
          </CardHeader>
          <CardContent>
            <Separator />
            <div className="grid gap-x-6 md:grid-cols-2">
              <FormField
                control={form.control}
                name="aadharNumber"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex flex-col gap-2">
                    <FormItem>
                      <FormLabel>Aadhar Number</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="enter aadhar number"
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
                      {watchAadharNumberRef.current && (
                        <FormDescription
                          className={cn(
                            watchAadharNumberRef.current?.length === 10 &&
                              "text-green-400",
                            watchAadharNumberRef.current?.length > 10 &&
                              "text-red-400",
                            "flex gap-3"
                          )}
                        >
                          {10 - watchAadharNumberRef.current?.length} digits
                          remaining.{" "}
                        </FormDescription>
                      )}
                    </FormItem>
                  </div>
                )}
              />
              <FormField
                control={form.control}
                name="nationality"
                render={({ fieldState }) => (
                  <div className="my-4 flex w-full flex-col gap-2">
                    <FormItem>
                      <FormLabel>Nationality</FormLabel>
                      <FormControl>
                        <div className="w-full">
                          <NationalitySelectDropdown
                            className={cn(
                              !fieldState.invalid && "border-green-400",
                              fieldState.error && "border-red-400",
                              "w-full"
                            )}
                            setValue={form.setValue}
                          />
                        </div>
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  </div>
                )}
              />
              <FormField
                control={form.control}
                name="firstName"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex w-full flex-col gap-2">
                    <FormItem>
                      <FormLabel>First Name</FormLabel>
                      <FormControl>
                        <Input
                          type="text"
                          className={cn(
                            fieldState.isDirty &&
                              !fieldState.invalid &&
                              "border-green-400",
                            fieldState.error && "border-red-400"
                          )}
                          placeholder="enter your first name"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  </div>
                )}
              />
              <FormField
                control={form.control}
                name="lastName"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex w-full flex-col gap-2">
                    <FormItem>
                      <FormLabel>Last Name / Sur Name</FormLabel>
                      <FormControl>
                        <Input
                          type="text"
                          className={cn(
                            fieldState.isDirty &&
                              !fieldState.invalid &&
                              "border-green-400",
                            fieldState.error && "border-red-400"
                          )}
                          placeholder="enter your last name"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  </div>
                )}
              />
              <FormField
                control={form.control}
                name="fatherName"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex w-full flex-col gap-2">
                    <FormItem>
                      <FormLabel>Father Name</FormLabel>
                      <FormControl>
                        <Input
                          type="text"
                          placeholder="enter your father's name"
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
                    </FormItem>
                  </div>
                )}
              />
              <FormField
                control={form.control}
                name="motherName"
                render={({ field, fieldState }) => (
                  <div className="my-4 flex w-full flex-col gap-2">
                    <FormItem>
                      <FormLabel>Mother Name</FormLabel>
                      <FormControl>
                        <Input
                          type="text"
                          className={cn(
                            fieldState.isDirty &&
                              !fieldState.invalid &&
                              "border-green-400",
                            fieldState.error && "border-red-400"
                          )}
                          placeholder="enter your mother's name"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
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
              {!!isFormSubmitting && (
                <Loader className="mr-4 animate-spin" />
              )}{" "}
              Submit
            </Button>
          </CardFooter>
        </Card>
      </form>
    </Form>
  );
};

export default SurveyForm;
