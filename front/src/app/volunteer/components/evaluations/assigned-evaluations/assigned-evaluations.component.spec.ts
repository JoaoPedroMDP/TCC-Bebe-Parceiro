import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AssignedEvaluationsComponent } from './assigned-evaluations.component';

describe('AssignedEvaluationsComponent', () => {
  let component: AssignedEvaluationsComponent;
  let fixture: ComponentFixture<AssignedEvaluationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AssignedEvaluationsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AssignedEvaluationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
