import 'package:flutter/material.dart';
import '../widgets/section_header.dart';

/// Data model for a skill entry.
class _SkillEntry {
  final String name;
  final double proficiency; // 0.0 – 1.0
  final IconData icon;

  const _SkillEntry({
    required this.name,
    required this.proficiency,
    required this.icon,
  });
}

/// A category of skills.
class _SkillCategory {
  final String title;
  final IconData icon;
  final Color color;
  final List<_SkillEntry> skills;

  const _SkillCategory({
    required this.title,
    required this.icon,
    required this.color,
    required this.skills,
  });
}

class SkillsExplorerScreen extends StatefulWidget {
  const SkillsExplorerScreen({super.key});

  @override
  State<SkillsExplorerScreen> createState() => _SkillsExplorerScreenState();
}

class _SkillsExplorerScreenState extends State<SkillsExplorerScreen>
    with SingleTickerProviderStateMixin {
  late final TabController _tabController;

  static const _categories = [
    _SkillCategory(
      title: 'Frontend',
      icon: Icons.web,
      color: Color(0xFF6750A4),
      skills: [
        _SkillEntry(name: 'Flutter / Dart', proficiency: 0.75, icon: Icons.phone_android),
        _SkillEntry(name: 'React / Next.js', proficiency: 0.90, icon: Icons.language),
        _SkillEntry(name: 'TypeScript', proficiency: 0.88, icon: Icons.code),
        _SkillEntry(name: 'HTML / CSS', proficiency: 0.92, icon: Icons.style),
        _SkillEntry(name: 'Tailwind CSS', proficiency: 0.85, icon: Icons.palette),
      ],
    ),
    _SkillCategory(
      title: 'Backend',
      icon: Icons.dns,
      color: Color(0xFF0061A4),
      skills: [
        _SkillEntry(name: 'Python / FastAPI', proficiency: 0.82, icon: Icons.snippet_folder),
        _SkillEntry(name: 'Node.js / Express', proficiency: 0.78, icon: Icons.hub),
        _SkillEntry(name: 'PostgreSQL', proficiency: 0.80, icon: Icons.storage),
        _SkillEntry(name: 'SQLite', proficiency: 0.75, icon: Icons.storage),
        _SkillEntry(name: 'REST APIs', proficiency: 0.88, icon: Icons.api),
      ],
    ),
    _SkillCategory(
      title: 'DevOps & Cloud',
      icon: Icons.cloud,
      color: Color(0xFF1B6E3D),
      skills: [
        _SkillEntry(name: 'Docker', proficiency: 0.72, icon: Icons.widgets),
        _SkillEntry(name: 'AWS', proficiency: 0.68, icon: Icons.cloud_queue),
        _SkillEntry(name: 'Vercel', proficiency: 0.90, icon: Icons.rocket_launch),
        _SkillEntry(name: 'Cloudflare Workers', proficiency: 0.75, icon: Icons.bolt),
        _SkillEntry(name: 'CI/CD', proficiency: 0.70, icon: Icons.sync),
      ],
    ),
    _SkillCategory(
      title: 'Tools & AI',
      icon: Icons.auto_awesome,
      color: Color(0xFF7D5260),
      skills: [
        _SkillEntry(name: 'Git / GitHub', proficiency: 0.88, icon: Icons.code),
        _SkillEntry(name: 'AI / LLM Integration', proficiency: 0.78, icon: Icons.psychology),
        _SkillEntry(name: 'Web Scraping', proficiency: 0.82, icon: Icons.bug_report),
        _SkillEntry(name: 'Automation', proficiency: 0.80, icon: Icons.smart_toy),
        _SkillEntry(name: 'Figma', proficiency: 0.65, icon: Icons.design_services),
      ],
    ),
  ];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: _categories.length, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;

    return CustomScrollView(
      physics: const AlwaysScrollableScrollPhysics(),
      slivers: [
        // Header
        SliverToBoxAdapter(
          child: Container(
            padding: const EdgeInsets.fromLTRB(24, 60, 24, 16),
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
                const SectionHeader(title: 'Skills Explorer'),
                const SizedBox(height: 8),
                Text(
                  'Interactive proficiency map across ${_totalSkills()} skills in ${_categories.length} categories.',
                  style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: colorScheme.onSurfaceVariant,
                      ),
                ),
                const SizedBox(height: 20),
                // Summary chips
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: _categories.map((cat) {
                    final avg = cat.skills
                            .map((s) => s.proficiency)
                            .reduce((a, b) => a + b) /
                        cat.skills.length;
                    return Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: cat.color.withValues(alpha: 0.12),
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(
                            color: cat.color.withValues(alpha: 0.3)),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(cat.icon, size: 14, color: cat.color),
                          const SizedBox(width: 6),
                          Text(
                            '${cat.title}: ${(avg * 100).round()}%',
                            style: Theme.of(context)
                                .textTheme
                                .labelSmall
                                ?.copyWith(
                                  color: cat.color,
                                  fontWeight: FontWeight.w600,
                                ),
                          ),
                        ],
                      ),
                    );
                  }).toList(),
                ),
              ],
            ),
          ),
        ),

        // Tab bar
        SliverToBoxAdapter(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24),
            child: TabBar(
              controller: _tabController,
              isScrollable: true,
              tabAlignment: TabAlignment.start,
              labelStyle: Theme.of(context).textTheme.labelLarge?.copyWith(
                    fontWeight: FontWeight.w600,
                  ),
              tabs: _categories
                  .map((cat) => Tab(
                        icon: Icon(cat.icon, size: 18),
                        text: cat.title,
                      ))
                  .toList(),
            ),
          ),
        ),

        // Tab content
        SliverFillRemaining(
          hasScrollBody: false,
          child: TabBarView(
            controller: _tabController,
            children: _categories.map((cat) {
              return ListView.builder(
                padding: const EdgeInsets.fromLTRB(24, 16, 24, 24),
                itemCount: cat.skills.length,
                itemBuilder: (context, index) {
                  final skill = cat.skills[index];
                  return _AnimatedSkillTile(
                    skill: skill,
                    color: cat.color,
                    delay: index * 100,
                  );
                },
              );
            }).toList(),
          ),
        ),
      ],
    );
  }

  int _totalSkills() =>
      _categories.fold(0, (sum, cat) => sum + cat.skills.length);
}

class _AnimatedSkillTile extends StatefulWidget {
  final _SkillEntry skill;
  final Color color;
  final int delay;

  const _AnimatedSkillTile({
    required this.skill,
    required this.color,
    required this.delay,
  });

  @override
  State<_AnimatedSkillTile> createState() => _AnimatedSkillTileState();
}

class _AnimatedSkillTileState extends State<_AnimatedSkillTile> {
  double _barFraction = 0.0;

  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(milliseconds: 300 + widget.delay), () {
      if (mounted) setState(() => _barFraction = widget.skill.proficiency);
    });
  }

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    final pct = (widget.skill.proficiency * 100).round();

    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: TweenAnimationBuilder<double>(
        tween: Tween(begin: 0.0, end: 1.0),
        duration: Duration(milliseconds: 500 + widget.delay),
        curve: Curves.easeOut,
        builder: (context, fadeValue, child) {
          return Opacity(
            opacity: fadeValue,
            child: Transform.translate(
              offset: Offset(0, 10 * (1 - fadeValue)),
              child: child,
            ),
          );
        },
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            border: Border.all(color: colorScheme.outlineVariant),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    width: 40,
                    height: 40,
                    decoration: BoxDecoration(
                      color: widget.color.withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Icon(widget.skill.icon,
                        size: 20, color: widget.color),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(
                      widget.skill.name,
                      style:
                          Theme.of(context).textTheme.titleSmall?.copyWith(
                                fontWeight: FontWeight.w600,
                              ),
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(
                        horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: widget.color.withValues(alpha: 0.1),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      '$pct%',
                      style:
                          Theme.of(context).textTheme.labelMedium?.copyWith(
                                color: widget.color,
                                fontWeight: FontWeight.bold,
                              ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              AnimatedBuilder(
                fraction: _barFraction,
                color: widget.color,
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Animated progress bar that fills to the given fraction.
class AnimatedBuilder extends StatelessWidget {
  final double fraction;
  final Color color;

  const AnimatedBuilder({
    super.key,
    required this.fraction,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return LayoutBuilder(
      builder: (context, constraints) {
        return TweenAnimationBuilder<double>(
          tween: Tween(begin: 0.0, end: fraction),
          duration: const Duration(milliseconds: 800),
          curve: Curves.easeOutCubic,
          builder: (context, value, _) {
            return Container(
              height: 8,
              decoration: BoxDecoration(
                color: colorScheme.surfaceContainerHighest,
                borderRadius: BorderRadius.circular(4),
              ),
              child: Align(
                alignment: Alignment.centerLeft,
                child: TweenAnimationBuilder<double>(
                  tween: Tween(begin: 0.0, end: value),
                  duration: const Duration(milliseconds: 100),
                  builder: (context, w, _) {
                    return Container(
                      width: constraints.maxWidth * w,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            color.withValues(alpha: 0.7),
                            color,
                          ],
                        ),
                        borderRadius: BorderRadius.circular(4),
                      ),
                    );
                  },
                ),
              ),
            );
          },
        );
      },
    );
  }
}
