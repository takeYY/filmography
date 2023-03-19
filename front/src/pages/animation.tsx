import styles from "@/styles/Home.module.css";
import type { NextPage } from "next";
import Head from "next/head";

const Animation: NextPage = () => {
  return (
    <>
      <Head>
        <title>Filmography</title>
        <meta name="description" content="Filmography" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <div className={styles.grid}>
          <p>アニメです</p>
          <p>アニメです</p>
          <p>アニメです</p>
          <p>アニメです</p>
          <p>アニメです</p>
          <p>アニメです</p>
          <p>アニメです</p>
        </div>
      </main>
    </>
  );
};

export default Animation;
