import type { NextPage } from "next";
import Head from "next/head";
import Link from "next/link";
import { Button } from "~/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "~/components/ui/card";

const terms_conditions = [
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "Nunc facilisis enim eget augue ullamcorper condimentum.",
  "Vivamus fringilla purus id nisi porta accumsan.",
  "Quisque feugiat sapien sed dignissim fermentum.",
  "Nullam tincidunt magna a neque viverra, vitae aliquet libero viverra.",
  "Vivamus ac leo cursus eros dictum faucibus vel eget massa.",
];

const SamaajMemberSurveyPage: NextPage = () => {
  return (
    <>
      <Head>
        <title>Rohit Samaaj | Survey Form</title>
        <meta name="description" content="rohit samaaj member survey form." />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="mx-auto my-2 max-w-2xl">
        <h2 className="text-2xl">Rohit Samaaj Members Survey</h2>
        <Card className="mt-4">
          <CardHeader>
            <CardTitle>Terms and conditions</CardTitle>
          </CardHeader>
          <CardContent>
            {terms_conditions.map((tc, idx) => (
              <p key={idx}>
                {idx + 1}. {tc}
              </p>
            ))}
          </CardContent>
        </Card>
        <Button className="mt-4">
          <Link href="/samaaj-member/survey/personal-details">
            Accept & Proceed
          </Link>
        </Button>
      </main>
    </>
  );
};

export default SamaajMemberSurveyPage;
