import React, { useState, useEffect } from 'react';

const About = () => {
  const [about, setAbout] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/about/')
      .then(res => res.json())
      .then(data => {
        setAbout(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching about info:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loader"></div>;
  if (!about) return <div className="container section text-center">No about information found.</div>;

  const getImageUrl = (image) => {
    if (!image) return null;
    return image.startsWith('http') ? image : `http://localhost:8000${image}`;
  };

  const profileImage = getImageUrl(about.profile_image);

  return (
    <div className="container section">
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '4rem', alignItems: 'center' }}>
        
        {/* Profile Image */}
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <div style={{ 
            width: '300px', 
            height: '300px', 
            borderRadius: '50%', 
            overflow: 'hidden',
            border: '4px solid var(--primary-color)',
            boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.5)'
          }}>
            {profileImage ? (
              <img src={profileImage} alt={about.name} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
            ) : (
              <div style={{ width: '100%', height: '100%', backgroundColor: 'var(--bg-secondary)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                No Image
              </div>
            )}
          </div>
        </div>

        {/* About Content */}
        <div>
          <h1 className="text-gradient" style={{ fontSize: '3rem', marginBottom: '1rem' }}>About Me</h1>
          <h2 style={{ color: 'var(--text-color)', marginBottom: '1.5rem', fontWeight: 500 }}>{about.name}</h2>
          
          <div style={{ color: 'var(--text-secondary)', marginBottom: '2rem', whiteSpace: 'pre-line', lineHeight: 1.8 }}>
            {about.bio}
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', backgroundColor: 'var(--bg-secondary)', padding: '2rem', borderRadius: '1rem', border: '1px solid var(--border-color)' }}>
            <h3 style={{ marginBottom: '1rem', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem' }}>Contact Info</h3>
            <div><strong>Email:</strong> <a href={`mailto:${about.email}`} style={{ color: 'var(--primary-color)' }}>{about.email}</a></div>
            {about.phone && <div><strong>Phone:</strong> {about.phone}</div>}
            {about.location && <div><strong>Location:</strong> {about.location}</div>}
            
            {about.resume && (
              <a href={getImageUrl(about.resume)} target="_blank" rel="noopener noreferrer" className="btn btn-primary" style={{ marginTop: '1rem', alignSelf: 'flex-start' }}>
                Download Resume
              </a>
            )}
          </div>
        </div>

      </div>
    </div>
  );
};

export default About;
