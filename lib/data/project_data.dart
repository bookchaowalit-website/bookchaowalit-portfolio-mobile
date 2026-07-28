import 'package:flutter/material.dart';

/// Centralized project data shared across screens.
class ProjectEntry {
  final String name;
  final String description;
  final String longDescription;
  final List<String> tags;
  final String url;
  final IconData icon;
  final List<String> features;

  const ProjectEntry({
    required this.name,
    required this.description,
    required this.longDescription,
    required this.tags,
    required this.url,
    required this.icon,
    required this.features,
  });
}

class ProjectData {
  static const List<ProjectEntry> allProjects = [
    ProjectEntry(
      name: 'Portfolio Web Platform',
      description: '100+ micro-frontends with i18n, dynamic routing, and dark mode deployed on Vercel.',
      longDescription:
          'A comprehensive portfolio platform built with Next.js featuring over 100 micro-frontends. '
          'Each section is independently deployable with full internationalization support (EN/TH), '
          'dynamic routing, and a monochrome design system. Deployed on Vercel with edge functions '
          'for optimal global performance.',
      tags: ['Next.js', 'TypeScript', 'Vercel'],
      url: 'https://bookchaowalit.com',
      icon: Icons.language,
      features: [
        '100+ independently deployable micro-frontends',
        'Multi-language support (EN/TH) with next-intl',
        'Dynamic OG image generation',
        'Edge functions for global low-latency',
        'Monochrome design system with dark mode',
        'Lighthouse 95+ performance score',
      ],
    ),
    ProjectEntry(
      name: 'Portfolio Mobile App',
      description: 'Cross-platform mobile app built with Flutter for iOS and Android.',
      longDescription:
          'A native-quality mobile portfolio app built with Flutter and Material Design 3. '
          'Features include animated splash screen, 5-tab navigation, 8 project showcases, '
          'interactive Skills Explorer with proficiency visualization, persistent favorites, '
          'real-time project search/filter, in-app contact form, vCard copy, '
          'pull-to-refresh, scroll animations, dark mode, share functionality, and deep linking. '
          'Designed to pass both Apple App Store and Google Play Store review guidelines.',
      tags: ['Flutter', 'Dart', 'Mobile'],
      url: 'https://github.com/bookchaowalit/bookchaowalit-portfolio-mobile',
      icon: Icons.phone_android,
      features: [
        'Material Design 3 with light/dark themes',
        'Animated splash screen with hero transition',
        '5-tab navigation with swipe gestures',
        'Interactive Skills Explorer with proficiency bars',
        'Persistent project favorites with SharedPreferences',
        'Real-time project search and filter',
        'In-app contact form with mailto integration',
        'vCard copy-to-clipboard for contacts app',
        'Pull-to-refresh and scroll animations',
        'In-app project detail pages',
        'Deep linking support for project URLs',
        'Settings with theme and language control',
      ],
    ),
    ProjectEntry(
      name: 'Base64 Encoder',
      description: 'Encode and decode Base64 strings in real time with file support.',
      longDescription:
          'A fast, client-side Base64 encoding and decoding tool. Supports text input, '
          'file upload with drag-and-drop, and real-time conversion. Built with Next.js '
          'and deployed on Vercel edge for instant loading worldwide.',
      tags: ['Next.js', 'React'],
      url: 'https://base64.bookchaowalit.com',
      icon: Icons.lock_outline,
      features: [
        'Real-time encode and decode',
        'File upload with drag-and-drop',
        'Client-side processing (no server)',
        'Copy to clipboard with one tap',
        'Responsive mobile-friendly UI',
      ],
    ),
    ProjectEntry(
      name: 'Regex Tester',
      description: 'Real-time regex testing with visual feedback and pattern library.',
      longDescription:
          'An interactive regex testing tool with real-time match highlighting, '
          'capture group visualization, and a curated pattern library. '
          'Supports JavaScript regex syntax with detailed match explanations.',
      tags: ['Next.js', 'React'],
      url: 'https://regex.bookchaowalit.com',
      icon: Icons.search,
      features: [
        'Real-time match highlighting',
        'Capture group visualization',
        'Curated pattern library',
        'JavaScript regex syntax support',
        'Match explanation and breakdown',
      ],
    ),
    ProjectEntry(
      name: 'Automation Platform',
      description: 'Cloudflare Workers-based automation system with scheduled tasks and API integrations.',
      longDescription:
          'A serverless automation platform built on Cloudflare Workers. Handles scheduled '
          'tasks, API integrations, and data pipelines. Features include cron-based scheduling, '
          'webhook triggers, and multi-service orchestration with error handling and retry logic.',
      tags: ['Python', 'Cloudflare', 'Workers'],
      url: 'https://github.com/bookchaowalit',
      icon: Icons.bolt,
      features: [
        'Serverless Cloudflare Workers architecture',
        'Cron-based task scheduling',
        'Webhook trigger support',
        'Multi-service orchestration',
        'Automatic retry with exponential backoff',
        'Real-time execution monitoring',
      ],
    ),
    ProjectEntry(
      name: 'Scraper Dashboard',
      description: 'Multi-source web scraping pipeline with deduplication and CSV export.',
      longDescription:
          'A full-featured web scraping platform with a real-time dashboard. '
          'Supports multiple data sources, intelligent deduplication, '
          'CSV/JSON export, and scheduled scraping jobs. Built with FastAPI backend '
          'and SQLite storage with concurrent write protection.',
      tags: ['Python', 'FastAPI', 'SQLite'],
      url: 'https://github.com/bookchaowalit',
      icon: Icons.dashboard,
      features: [
        'Multi-source scraping with dynamic dispatch',
        'Intelligent URL and content deduplication',
        'Real-time dashboard with live updates',
        'CSV and JSON export',
        'Scheduled scraping with cron jobs',
        'SQLite with concurrent write protection',
      ],
    ),
    ProjectEntry(
      name: 'JSON Formatter',
      description: 'Format, validate, and minify JSON with syntax highlighting.',
      longDescription:
          'A lightweight JSON formatting tool with syntax highlighting, validation, '
          'and minification. Features tree view for nested structures, error highlighting '
          'with line numbers, and one-click copy. Client-side only for data privacy.',
      tags: ['Next.js', 'TypeScript'],
      url: 'https://json.bookchaowalit.com',
      icon: Icons.data_object,
      features: [
        'Format, validate, and minify JSON',
        'Syntax highlighting with line numbers',
        'Tree view for nested structures',
        'Error highlighting with details',
        'Client-side processing for privacy',
      ],
    ),
    ProjectEntry(
      name: 'Color Converter',
      description: 'Convert between HEX, RGB, HSL, and HSV color formats.',
      longDescription:
          'A comprehensive color conversion tool supporting HEX, RGB, HSL, and HSV formats. '
          'Features a visual color picker, real-time conversion, CSS code generation, '
          'and a palette history. Useful for designers and developers working across different color systems.',
      tags: ['Next.js', 'React'],
      url: 'https://color.bookchaowalit.com',
      icon: Icons.palette,
      features: [
        'Convert between HEX, RGB, HSL, HSV',
        'Visual color picker',
        'CSS code generation',
        'Palette history tracking',
        'Real-time preview',
      ],
    ),
  ];
}
