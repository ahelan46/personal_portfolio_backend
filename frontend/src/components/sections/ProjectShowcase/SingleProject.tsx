"use client";

import React from "react";
import styles from "./SingleProject.module.css";
import { useLang, L } from "@/lib/i18n";

export default function SingleProject({ project, index }: { project: any, index: number }) {
  const { lang } = useLang();
  
  // Format index to be two digits
  const paddedIndex = String(index + 1).padStart(2, "0");
  
  // Resolve image URL
  const imageUrl = project.image 
    ? (project.image.startsWith('http') ? project.image : `http://localhost:8000${project.image}`) 
    : (project.cover?.src || '');
    
  // Resolve localized text
  const title = project.title || L(lang, project, "title");
  const description = project.short_description || L(lang, project, "contribution") || project.description;
  const tags = project.technology_used 
    ? project.technology_used.split(',').map((t: string) => t.trim().toUpperCase()).join(" · ")
    : ((project.fr && lang === "fr" ? project.fr.tags ?? project.tags : project.tags) || []).join(" · ").toUpperCase();

  return (
    <article className={styles.container}>
      <div className={styles.content}>
        <p className={styles.eyebrow}>
          <span>{paddedIndex}</span> Project
        </p>
        
        <h2 className={styles.title}>{title}</h2>
        <p className={styles.description}>{description}</p>
        
        <div className={styles.meta}>
          <div className={styles.metaRow}>
            {project.year && (
              <div className={styles.metaItem}>
                <span className={styles.metaLabel}>Year</span>
                <span className={styles.metaValue}>{project.year}</span>
              </div>
            )}
            {tags && (
              <div className={styles.metaItem}>
                <span className={styles.metaLabel}>Technology</span>
                <span className={styles.metaValue}>{tags}</span>
              </div>
            )}
          </div>
        </div>
        
        <div className={styles.links}>
          {(project.site?.url || project.project_url) && (
            <a 
              href={project.site?.url || project.project_url} 
              className={styles.linkBtn} 
              target="_blank" 
              rel="noreferrer"
            >
              Live Site <i aria-hidden="true">↗</i>
            </a>
          )}
          {(project.repo || project.github_url) && (
            <a 
              href={project.repo || project.github_url} 
              className={styles.linkBtn} 
              target="_blank" 
              rel="noreferrer"
            >
              GitHub <i aria-hidden="true">↗</i>
            </a>
          )}
        </div>
      </div>
      
      {imageUrl && (
        <div className={styles.imageWrap}>
          <img src={imageUrl} alt={title} loading="lazy" />
        </div>
      )}
    </article>
  );
}
