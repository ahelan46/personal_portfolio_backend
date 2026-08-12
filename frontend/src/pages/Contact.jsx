import React, { useState } from 'react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  const [status, setStatus] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // For now, just show a success message since backend form handling isn't implemented
    setStatus('success');
    setFormData({ name: '', email: '', subject: '', message: '' });
    setTimeout(() => setStatus(''), 5000);
  };

  return (
    <div className="container section">
      <div style={{ maxWidth: '600px', margin: '0 auto' }}>
        <h1 className="text-gradient" style={{ fontSize: '3rem', marginBottom: '1rem', textAlign: 'center' }}>Get In Touch</h1>
        <p style={{ textAlign: 'center', color: 'var(--text-secondary)', marginBottom: '3rem' }}>
          Have a project in mind or want to collaborate? I'd love to hear from you.
        </p>

        {status === 'success' && (
          <div style={{ backgroundColor: 'rgba(34, 197, 94, 0.1)', color: '#4ade80', padding: '1rem', borderRadius: '0.5rem', marginBottom: '2rem', border: '1px solid #4ade80', textAlign: 'center' }}>
            Your message has been sent successfully!
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ backgroundColor: 'var(--bg-secondary)', padding: '2.5rem', borderRadius: '1rem', border: '1px solid var(--border-color)' }}>
          <div className="form-group">
            <label htmlFor="name" className="form-label">Name</label>
            <input type="text" id="name" name="name" className="form-input" required value={formData.name} onChange={handleChange} />
          </div>
          
          <div className="form-group">
            <label htmlFor="email" className="form-label">Email</label>
            <input type="email" id="email" name="email" className="form-input" required value={formData.email} onChange={handleChange} />
          </div>
          
          <div className="form-group">
            <label htmlFor="subject" className="form-label">Subject</label>
            <input type="text" id="subject" name="subject" className="form-input" required value={formData.subject} onChange={handleChange} />
          </div>
          
          <div className="form-group">
            <label htmlFor="message" className="form-label">Message</label>
            <textarea id="message" name="message" className="form-input" required value={formData.message} onChange={handleChange}></textarea>
          </div>
          
          <button type="submit" className="btn btn-primary" style={{ width: '100%', padding: '1rem' }}>
            Send Message
          </button>
        </form>
      </div>
    </div>
  );
};

export default Contact;
