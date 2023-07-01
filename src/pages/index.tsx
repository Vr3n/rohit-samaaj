import { type NextPage } from "next";
import Head from "next/head";
import Link from "next/link";
import { Button } from "~/components/ui/button";

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>Rohit Samaaj | Home</title>
        <meta name="description" content="rohit samaaj home" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="mx-auto my-2 max-w-2xl">
        <Link href="/samaaj-member/survey">
          <Button>Add Samaaj Member</Button>
        </Link>
      </main>
    </>
  );
};

export default Home;
