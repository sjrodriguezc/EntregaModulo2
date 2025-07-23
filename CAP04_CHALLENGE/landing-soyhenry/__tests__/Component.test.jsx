import React from 'react'; 
import { render, screen } from '@testing-library/react';
import Component from '../components/LandingPage';

describe('Component', () => {
  it('muestra el título principal', () => {
    render(<Component />);
    expect(screen.getByText(/comienza o acelera tu carrera en tecnología/i)).toBeInTheDocument();
  });

  it('muestra la descripción', () => {
    render(<Component />);
    expect(screen.getByText(/estudia desarrollo full stack, data science o data analytics/i)).toBeInTheDocument();
  });
});