import { Button } from "@/components/ui/button"
import { ChevronDown, Monitor, BookOpen, Users, Shield } from "lucide-react"
import Image from "next/image"
import Link from "next/link"

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="bg-white border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <div className="flex-shrink-0">
              <Link href="/" className="flex items-center">
                <div className="text-2xl font-black tracking-wider">
                  <span className="text-yellow-400">H</span>
                  <span className="text-black">E</span>
                  <span className="text-yellow-400">N</span>
                  <span className="text-black">R</span>
                  <span className="text-yellow-400">Y</span>
                </div>
              </Link>
            </div>

            {/* Navigation Links */}
            <div className="hidden md:flex items-center space-x-8">
              <Link
                href="/estudiantes"
                className="flex items-center text-gray-700 hover:text-gray-900 text-sm font-medium"
              >
                Para estudiantes
                <ChevronDown className="ml-1 h-4 w-4" />
              </Link>
              <Link
                href="/empresas"
                className="flex items-center text-gray-700 hover:text-gray-900 text-sm font-medium"
              >
                Para empresas
                <ChevronDown className="ml-1 h-4 w-4" />
              </Link>
            </div>

            {/* Action Buttons */}
            <div className="flex items-center space-x-4">
              <Button variant="ghost" className="text-gray-700 hover:text-gray-900 font-medium">
                Ingresar
              </Button>
              <Button className="bg-yellow-400 hover:bg-orange-400 text-black font-bold px-6 py-2 rounded-lg">
                Aplicar
              </Button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          {/* Content */}
          <div className="space-y-8">
            <div className="space-y-6">
              <h1 className="text-5xl lg:text-6xl font-bold text-gray-900 leading-tight">
                Comienza o acelera tu carrera en tecnología
              </h1>
              <p className="text-xl text-gray-700 font-medium">
                Estudia Desarrollo Full Stack, Data Science o Data Analytics.
              </p>
            </div>

            {/* Features List */}
            <div className="space-y-6">
              <div className="flex items-center space-x-4">
                <div className="flex-shrink-0">
                  <Monitor className="h-6 w-6 text-purple-500" />
                </div>
                <span className="text-lg text-gray-800 font-medium">Online, en vivo y flexible</span>
              </div>

              <div className="flex items-center space-x-4">
                <div className="flex-shrink-0">
                  <BookOpen className="h-6 w-6 text-purple-500" />
                </div>
                <span className="text-lg text-gray-800 font-medium">Basado en proyectos</span>
              </div>

              <div className="flex items-center space-x-4">
                <div className="flex-shrink-0">
                  <Users className="h-6 w-6 text-purple-500" />
                </div>
                <span className="text-lg text-gray-800 font-medium">Basado en cohortes</span>
              </div>

              <div className="flex items-center space-x-4">
                <div className="flex-shrink-0">
                  <Shield className="h-6 w-6 text-purple-500" />
                </div>
                <span className="text-lg text-gray-800 font-medium">Garantía de Empleo</span>
              </div>
            </div>

            {/* CTA Button */}
            <div className="pt-4">
              <Button
                size="lg"
                className="bg-yellow-400 hover:bg-orange-400 text-black font-bold text-lg px-8 py-4 h-auto rounded-lg"
              >
                Aplicar
              </Button>
            </div>
          </div>

          {/* Image */}
          <div className="relative">
            <div className="relative rounded-3xl overflow-hidden">
              <Image
                src="/placeholder.webp"
                alt="Estudiante trabajando en su computadora en un ambiente moderno de estudio"
                width={600}
                height={600}
                className="w-full h-auto object-cover"
                priority
              />
            </div>
          </div>
        </div>
      </main>

      {/* Bottom Banner */}
      <div className="bg-white py-8 border-t border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-2xl font-bold text-gray-900">
              Bootcamp <span className="text-purple-600">#1</span> de Latam
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
