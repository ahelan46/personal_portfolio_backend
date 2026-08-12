/* Single source of truth for site-wide constants.
   Set NEXT_PUBLIC_SITE_URL in Vercel once the domain exists —
   everything (sitemap, robots, OG, JSON-LD) follows automatically. */

export const SITE_URL =
  (import.meta.env && import.meta.env.VITE_SITE_URL) || "http://localhost:5173";

export const PERSON = {
  name: "Ahelan Kumar Reddy Kolli",
  jobTitle: "Product Designer & UX Consultant",
  email: "kolligireeshkumarreddy0622@gmail.com",
  location: "Antibes, France",
  /* exact profile URLs as supplied — also consumed by JSON-LD */
  sameAs: [
    "https://www.linkedin.com/in/gireesh-kumar-reddy-kolli-",
    "https://github.com/gireeshkumarreddy",
    "https://www.instagram.com/itsgireeshreddy",
  ],
};
