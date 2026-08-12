"use client";

import { useEffect, useRef, useState } from "react";
import { gsap, ScrollTrigger, prefersReducedMotion, EASE } from "@/lib/gsap";
import Button from "@/components/ui/Button";
import VelocityMarquee from "@/components/ui/VelocityMarquee";
import styles from "./About.module.css";
import { useLang } from "@/lib/i18n";

type AboutData = {
  heading_1: string;
  heading_2: string;
  heading_em: string;
  heading_3: string;
  fr_heading_1: string;
  fr_heading_2: string;
  fr_heading_em: string;
  fr_heading_3: string;
  education_text: string;
  fr_education_text: string;
  cta_text: string;
  fr_cta_text: string;
  marquee_1: string[];
  marquee_2: string[];
  metrics: {
    value: string;
    count: number | null;
    prefix?: string;
    suffix?: string;
    label: string;
    fr_label: string;
  }[];
};

export default function About() {
  const root = useRef<HTMLElement>(null);
  const { t, lang } = useLang();
  
  const [aboutData, setAboutData] = useState<AboutData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/about/")
      .then((res) => res.json())
      .then((data) => {
        // Since there is only one About object, if it's a paginated list, we take the first.
        // The API actually returns a single object or list depending on the viewset. Let's handle both:
        const item = data.results ? data.results[0] : data[0] || data;
        setAboutData(item);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch about data:", err);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    const el = root.current;
    if (!el || loading || !aboutData || prefersReducedMotion()) return;

    const ctx = gsap.context(() => {
      /* shared reveal grammar — same as hero: y + fade, soft expo */
      const reveal = (targets: gsap.TweenTarget, trigger: Element, vars: gsap.TweenVars = {}) =>
        gsap.from(targets, {
          y: 44,
          autoAlpha: 0,
          duration: 1,
          ease: EASE.outExpo,
          stagger: 0.1,
          immediateRender: false,
          scrollTrigger: { trigger, start: "top 82%" },
          ...vars,
        });

      reveal([`.${styles.eyebrow}`, `.${styles.h2}`], el.querySelector(`.${styles.header}`)!);

      /* metrics: reveal + count-up when the band enters */
      const band = el.querySelector(`.${styles.metrics}`);
      if (band) {
        reveal(`.${styles.metric}`, band, { stagger: 0.09 });
        ScrollTrigger.create({
          trigger: band,
          start: "top 84%",
          once: true,
          onEnter: () => {
            gsap.utils.toArray<HTMLElement>("[data-metric-count]").forEach((numEl) => {
              const target = Number(numEl.dataset.metricCount);
              const obj = { v: 0 };
              /* the markup ships the real number, so it is correct with no JS
                 at all; the count-up rewinds to zero only at the moment it is
                 actually about to run */
              numEl.textContent = "0";
              gsap.to(obj, {
                v: target,
                duration: 1.4,
                ease: "power2.out",
                onUpdate: () => {
                  numEl.textContent = String(Math.round(obj.v));
                },
              });
            });
          },
        });
      }

      reveal(
        [`.${styles.edu}`, `.${styles.next}`],
        el.querySelector(`.${styles.edu}`)!,
        { stagger: 0.12 }
      );
    }, el);

    return () => ctx.revert();
  }, [loading, aboutData]);

  if (!aboutData) return <section className={styles.about} id="about" ref={root}></section>;

  const isFr = lang === "fr";

  return (
    <section className={styles.about} id="about" ref={root}>
      <VelocityMarquee rows={[
        { items: aboutData.marquee_1 || [], velocity: 34 },
        { items: aboutData.marquee_2 || [], velocity: -28, outline: true }
      ]} />

      <div className={styles.wrap}>
        <div className={styles.header}>
          <p className={styles.eyebrow}>
            <span>01</span> {t("about.eyebrow")}
          </p>
          <h2 className={styles.h2}>
            {isFr && aboutData.fr_heading_1 ? aboutData.fr_heading_1 : aboutData.heading_1}<br />
            {isFr && aboutData.fr_heading_2 ? aboutData.fr_heading_2 : aboutData.heading_2} <em className={styles.serif}>{isFr && aboutData.fr_heading_em ? aboutData.fr_heading_em : aboutData.heading_em}</em>{(isFr && aboutData.fr_heading_3) ? aboutData.fr_heading_3 : aboutData.heading_3}
          </h2>
        </div>

        <div className={styles.metrics}>
          {(aboutData.metrics || []).map((m, idx) => (
            <div className={styles.metric} key={idx}>
              <div className={styles.metricNum}>
                {m.count !== null ? (
                  <>
                    {m.prefix}
                    <span data-metric-count={m.count}>{m.count}</span>
                    <i>{m.suffix}</i>
                  </>
                ) : (
                  <span className={styles.metricStatic}>{m.value}</span>
                )}
              </div>
              <div className={styles.metricLabel}>{isFr && m.fr_label ? m.fr_label : m.label}</div>
            </div>
          ))}
        </div>

        <p className={styles.edu}>
          {isFr && aboutData.fr_education_text ? aboutData.fr_education_text : aboutData.education_text}
        </p>

        <div className={styles.next}>
          <Button href="#work" variant="dark" size="sm" arrow>
            {isFr && aboutData.fr_cta_text ? aboutData.fr_cta_text : aboutData.cta_text}
          </Button>
        </div>
      </div>
    </section>
  );
}
