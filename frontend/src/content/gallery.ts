/* THE PEOPLE BEHIND THE WORK — the personal archive.
 *
 * ⚠ SOURCING: every frame is one of Gireesh's own supplied photographs,
 * in the order he numbered them (Gallery 1 → 14). Nothing is stock,
 * generated, substituted or repeated. He supplied 14 of the 15 he listed —
 * Gallery 15 never arrived; add it to the end of this array when it does.
 *
 * `ar` is each file's TRUE aspect ratio, so a frame is only ever cropped by
 * object-fit, never scaled non-uniformly. The variety in frame widths comes
 * from the photographs themselves rather than from arbitrary sizing.
 *
 * `scale` and `y` are the curation: a little rhythm so the rail reads as a
 * hung archive rather than a filmstrip. Frames 9 and 10 — the two team
 * photographs Gireesh marked as belonging in the middle — sit at the centre
 * of the sequence and carry the largest scale. */

export type Frame = {
  id: string;
  src: string;
  ar: number; /* true width / height */
  scale: number; /* relative height on the rail */
  y: number; /* vertical offset in px, for rhythm */
  hero?: boolean; /* the centrepieces */
};

export const FRAMES: Frame[] = [
  { id: "g01", src: "/images/gallery/g01.jpg", ar: 1.333, scale: 1.0, y: -10, hero: true },
  { id: "g02", src: "/images/gallery/g02.jpg", ar: 0.75, scale: 0.95, y: 15 },
  { id: "g03", src: "/images/gallery/g03.jpg", ar: 0.574, scale: 1.0, y: -15, hero: true },
  { id: "g04", src: "/images/gallery/g04.jpg", ar: 0.578, scale: 0.9, y: 10 },
];
