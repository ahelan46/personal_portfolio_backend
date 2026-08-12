import React from 'react';

const Footer = () => {
  return (
    <footer style={{ borderTop: '1px solid var(--border-color)', padding: '2rem 0', marginTop: '4rem', backgroundColor: 'var(--bg-secondary)', textAlign: 'center' }}>
      <div className="container">
        <p style={{ color: 'var(--text-secondary)' }}>
          &copy; {new Date().getFullYear()} Portfolio. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
