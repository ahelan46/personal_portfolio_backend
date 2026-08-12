import React, { useState, useEffect } from 'react';
import Nav from "@/components/layout/Nav";
import Scene from "@/components/layout/Scene";
import TunnelIntro from "@/components/sections/Intro/TunnelIntro";
import Hero from "@/components/sections/Hero/Hero";
import About from "@/components/sections/About/About";
import Journey from "@/components/sections/Journey/LightJourney";
import DesignStack from "@/components/sections/Stack/DesignStack";
import Work from "@/components/sections/Work/Work";
import Experience from "@/components/sections/Experience/Experience";
import Certifications from "@/components/sections/Certifications/Certifications";
import Gallery from "@/components/sections/Gallery/Gallery";
import { ConnectHero, ConnectForm } from "@/components/sections/Connect/Connect";
import SingleProject from "@/components/sections/ProjectShowcase/SingleProject";

export default function Home() {
  const [projects, setProjects] = useState();
  const [skills, setSkills] = useState();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
        const [projectsRes, skillsRes] = await Promise.all([
          fetch(`${apiUrl}/api/projects/`),
          fetch(`${apiUrl}/api/skills/`)
        ]);
        
        const projectsData = await projectsRes.json();
        const skillsData = await skillsRes.json();
        
        setProjects(projectsData.results || projectsData);
        setSkills(skillsData.results || skillsData);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: '#000', color: '#fff' }}>Loading...</div>;

  return (
    <>
      <Nav />
      <main>
        <Scene order={1} runway={6} id="intro" keepOnMobile>
          <TunnelIntro />
        </Scene>

        <Scene order={2} id="hero">
          <Hero />
        </Scene>

        <Scene order={3} id="about">
          <About />
        </Scene>

        <Scene order={4} runway={6} id="journey" keepOnMobile>
          <Journey />
        </Scene>

        <Scene order={5} id="stack">
          <DesignStack skills={skills} />
        </Scene>

        <Scene order={6} runway={4.5} id="work">
          <Work projects={projects} />
        </Scene>

        <Scene order={7} runway={4.4} id="experience">
          <Experience />
        </Scene>

        <Scene order={8} runway={3.5} id="credentials">
          <Certifications />
        </Scene>

        {projects && projects.map((project, index) => (
          <Scene key={project.id || index} order={9 + index} id={`project-${project.id || index}`} keepOnMobile>
            <SingleProject project={project} index={index} />
          </Scene>
        ))}

        <Scene order={9 + (projects?.length || 0)} runway={1.6} id="gallery" keepOnMobile>
          <Gallery />
        </Scene>

        <Scene order={10 + (projects?.length || 0)} id="contact-hero" keepOnMobile>
          <ConnectHero />
        </Scene>

        <Scene order={11 + (projects?.length || 0)} id="contact-form" keepOnMobile>
          <ConnectForm />
        </Scene>
      </main>
    </>
  );
}
