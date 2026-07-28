import 'package:flutter/material.dart';
import '../widgets/section_header.dart';
import '../widgets/skill_chip.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;

    return CustomScrollView(
      physics: const AlwaysScrollableScrollPhysics(),
      slivers: [
        // Header
        SliverToBoxAdapter(
          child: Container(
            padding: const EdgeInsets.fromLTRB(24, 60, 24, 24),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  colorScheme.primaryContainer.withValues(alpha: 0.2),
                  colorScheme.surface,
                ],
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SectionHeader(title: 'About Me'),
                const SizedBox(height: 12),
                Text(
                  'Generalist & Solopreneur who enjoys solving problems and building things end-to-end.',
                  style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: colorScheme.onSurfaceVariant,
                      ),
                ),
              ],
            ),
          ),
        ),

        // Experience
        SliverToBoxAdapter(
          child: _AnimatedSection(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(24, 32, 24, 0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SectionHeader(title: 'Experience'),
                  const SizedBox(height: 16),
                  _ExperienceCard(
                    title: 'Freelance Developer',
                    company: 'Self-employed',
                    period: '2023 — Present',
                    description: 'Building full-stack web and mobile applications for clients. Specializing in Next.js, Flutter, and automation systems.',
                  ),
                  const SizedBox(height: 12),
                  _ExperienceCard(
                    title: 'Full-Stack Developer',
                    company: 'Various Projects',
                    period: '2022 — Present',
                    description: 'Developed 100+ micro-frontends, automation pipelines, and mobile apps using modern tech stacks.',
                  ),
                  const SizedBox(height: 12),
                  _ExperienceCard(
                    title: 'Solopreneur',
                    company: 'Solo Empire',
                    period: '2024 — Present',
                    description: 'Building and scaling digital products, content platforms, and developer tools from concept to deployment.',
                  ),
                ],
              ),
            ),
          ),
        ),

        // Education
        SliverToBoxAdapter(
          child: _AnimatedSection(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(24, 32, 24, 0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SectionHeader(title: 'Education'),
                  const SizedBox(height: 16),
                  _ExperienceCard(
                    title: 'Computer Science',
                    company: 'Chitralada University',
                    period: 'Bangkok, Thailand',
                    description: 'Focus on software engineering, algorithms, and full-stack development.',
                  ),
                ],
              ),
            ),
          ),
        ),

        // Skills
        SliverToBoxAdapter(
          child: _AnimatedSection(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(24, 32, 24, 0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SectionHeader(title: 'Skills'),
                  const SizedBox(height: 16),
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: const [
                      SkillChip(label: 'Flutter'),
                      SkillChip(label: 'Dart'),
                      SkillChip(label: 'Next.js'),
                      SkillChip(label: 'React'),
                      SkillChip(label: 'TypeScript'),
                      SkillChip(label: 'JavaScript'),
                      SkillChip(label: 'Python'),
                      SkillChip(label: 'FastAPI'),
                      SkillChip(label: 'Node.js'),
                      SkillChip(label: 'PostgreSQL'),
                      SkillChip(label: 'SQLite'),
                      SkillChip(label: 'Docker'),
                      SkillChip(label: 'AWS'),
                      SkillChip(label: 'Cloudflare'),
                      SkillChip(label: 'Vercel'),
                      SkillChip(label: 'Git'),
                      SkillChip(label: 'CI/CD'),
                      SkillChip(label: 'Material Design 3'),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),

        // Languages
        SliverToBoxAdapter(
          child: _AnimatedSection(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(24, 32, 24, 24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SectionHeader(title: 'Languages'),
                  const SizedBox(height: 16),
                  _LanguageBar(language: 'Thai', level: 1.0),
                  const SizedBox(height: 12),
                  _LanguageBar(language: 'English', level: 0.8),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class _ExperienceCard extends StatelessWidget {
  final String title;
  final String company;
  final String period;
  final String description;

  const _ExperienceCard({
    required this.title,
    required this.company,
    required this.period,
    required this.description,
  });

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        border: Border.all(color: colorScheme.outlineVariant),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Text(
                  title,
                  style: Theme.of(context).textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.w600,
                      ),
                ),
              ),
              Text(
                period,
                style: Theme.of(context).textTheme.bodySmall?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                    ),
              ),
            ],
          ),
          const SizedBox(height: 4),
          Text(
            company,
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: colorScheme.primary,
                  fontWeight: FontWeight.w500,
                ),
          ),
          const SizedBox(height: 8),
          Text(
            description,
            style: Theme.of(context).textTheme.bodySmall?.copyWith(
                  color: colorScheme.onSurfaceVariant,
                ),
          ),
        ],
      ),
    );
  }
}

class _LanguageBar extends StatelessWidget {
  final String language;
  final double level;

  const _LanguageBar({required this.language, required this.level});

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(language, style: Theme.of(context).textTheme.bodyMedium),
            Text(
              level >= 1.0 ? 'Native' : 'Professional',
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant,
                  ),
            ),
          ],
        ),
        const SizedBox(height: 6),
        ClipRRect(
          borderRadius: BorderRadius.circular(4),
          child: LinearProgressIndicator(
            value: level,
            backgroundColor: colorScheme.surfaceContainerHighest,
            color: colorScheme.primary,
            minHeight: 6,
          ),
        ),
      ],
    );
  }
}

class _AnimatedSection extends StatelessWidget {
  const _AnimatedSection({required this.child});
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0.0, end: 1.0),
      duration: const Duration(milliseconds: 600),
      curve: Curves.easeOut,
      builder: (context, value, child) {
        return Opacity(
          opacity: value,
          child: Transform.translate(
            offset: Offset(0, 20 * (1 - value)),
            child: child,
          ),
        );
      },
      child: child,
    );
  }
}
