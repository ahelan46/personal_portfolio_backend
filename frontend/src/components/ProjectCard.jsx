import React from 'react';

const ProjectCard = ({ project }) => {
  const getImageUrl = (image) => {
    if (!image) return null;
    return image.startsWith('http') ? image : `http://localhost:8000${image}`;
  };

  const imageUrl = getImageUrl(project.image);
  
  const techList = project.technology_used 
    ? project.technology_used.split(',').map(tech => tech.trim())
    : [];

  return (
    <div className="card">
      {imageUrl ? (
        <div className="card-img-container">
          <img src={imageUrl} alt={project.title} className="card-img" />
        </div>
      ) : (
        <div className="card-img-container" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <span style={{ color: 'var(--text-secondary)' }}>No Image</span>
        </div>
      )}
      <div className="card-content">
        <h3 className="card-title">{project.title}</h3>
        <p className="card-desc">{project.short_description || project.description.substring(0, 100) + '...'}</p>
        
        <div className="card-tags">
          {techList.slice(0, 4).map((tech, index) => (
            <span key={index} className="tag">{tech}</span>
          ))}
          {techList.length > 4 && <span className="tag">+{techList.length - 4}</span>}
        </div>
        
        <div style={{ display: 'flex', gap: '1rem', marginTop: 'auto' }}>
          {project.project_url && (
            <a href={project.project_url} target="_blank" rel="noopener noreferrer" className="btn btn-primary" style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}>
              View Live
            </a>
          )}
          {project.github_url && (
            <a href={project.github_url} target="_blank" rel="noopener noreferrer" className="btn" style={{ border: '1px solid var(--border-color)', padding: '0.5rem 1rem', fontSize: '0.875rem' }}>
              GitHub
            </a>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProjectCard;
