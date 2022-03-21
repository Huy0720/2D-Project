package sat;

import immutable.EmptyImList;
import immutable.ImList;
import immutable.ImListIterator;
import sat.env.Environment;
import sat.env.Variable;
import sat.formula.Clause;
import sat.formula.Formula;
import sat.formula.Literal;
import sat.formula.PosLiteral;

/**
 * A simple DPLL SAT solver. See http://en.wikipedia.org/wiki/DPLL_algorithm
 */
public class SATSolver {
    /**
     * Solve the problem using a simple version of DPLL with backtracking and
     * unit propagation. The returned environment binds literals of class
     * bool.Variable rather than the special literals used in clausification of
     * class clausal.Literal, so that clients can more readily use it.
     * 
     * @return an environment for which the problem evaluates to Bool.TRUE, or
     *         null if no such environment exists.
     */
    public static Environment solve(Formula formula) {

        Environment env = new Environment();
        ImList<Clause> clauses = formula.getClauses();
        return solve(clauses, env);
    }

    /**
     * Takes a partial assignment of variables to values, and recursively
     * searches for a complete satisfying assignment.
     * 
     * @param clauses
     *            formula in conjunctive normal form
     * @param env
     *            assignment of some or all variables in clauses to true or
     *            false values.
     * @return an environment for which all the clauses evaluate to Bool.TRUE,
     *         or null if no such environment exists.
     */
    private static Environment solve(ImList<Clause> clauses, Environment env) {

        //if no clause, formula is trivially satisfiable
        if (clauses.isEmpty()) {return env;}

        Clause smallest = clauses.first();
        for (Clause c:clauses) {
            // If empty clause, the clause list is unsatisfiable -- fail and backtrack.
            if (c.isEmpty()) {
                return null;
            }

            // Else, find the smallest clause (by number of literals)
            if (c.size() < smallest.size()) {
                smallest = c;
            }
            if (smallest.isUnit()) {
                smallest = c;
                break;
            }
        }

        Literal literal = smallest.chooseLiteral();
        Variable var = literal.getVariable();

        // if minimum size is 1, use it and recursively solve.
        if (smallest.isUnit()) {
            Environment newEnv;
            ImList<Clause> newClauses;
            if (literal instanceof PosLiteral) {
                newEnv = env.putTrue(literal.getVariable());
                newClauses = substitute(clauses,literal);
            } else {
                newEnv = env.putFalse(literal.getVariable());
                newClauses = substitute(clauses,literal);
            }
            return solve(newClauses, newEnv);
            }

        else {
            Environment newEnv;
            env = env.putTrue(var);
            // Set literal to TRUE, substitute for it in all the clauses, then solve recursively
            newEnv = solve(substitute(clauses, literal), env);
            if (newEnv == null) return solve(substitute(clauses, literal.getNegation()), env);
            else return newEnv;
        }
    }


    /**
     * given a clause list and literal, produce a new list resulting from
     * setting that literal to true
     * 
     * @param clauses
     *            , a list of clauses
     * @param l
     *            , a literal to set to true
     * @return a new list of clauses resulting from setting l to true
     */
    private static ImList<Clause> substitute(ImList<Clause> clauses,
            Literal l) {
        
        ImList<Clause> new_list= new EmptyImList<>();
        Clause clause = new Clause();
        for (Clause c:clauses) {
            if (c != null) clause = c.reduce(l);
            if (clause != null) new_list = new_list.add(clause);
        }
        return new_list;
    }

}
